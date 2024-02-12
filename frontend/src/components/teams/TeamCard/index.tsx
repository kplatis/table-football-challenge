'use client'

import { Player } from '@/types/players'
import { Badge, Button, Card, Center, Group, Text } from '@mantine/core'
import classes from './TeamCard.module.css'
import { IconUsers } from '@tabler/icons-react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

type TeamCardProps = {
  id: number
  name: string
  firstPlayer: Player
  secondPlayer?: Player
}

export default function TeamCard({
  id,
  name,
  firstPlayer,
  secondPlayer,
}: TeamCardProps) {
  const router = useRouter()
  return (
    <Card withBorder radius="md" className={classes.card}>
      <Group justify="space-between" mt="md">
        <Text fw={800}>{name}</Text>
      </Group>

      <Card.Section className={classes.section} mt="md">
        <Text fz="sm" c="dimmed" className={classes.label}>
          Players
        </Text>

        <Group gap={8} mb={-8}>
          <Center>
            <IconUsers size="1.05rem" className={classes.icon} stroke={1.5} />
            <Badge variant="outline" className="ml-2">
              <Link href={`/players/${firstPlayer.id}`}>
                {firstPlayer.name}
              </Link>
            </Badge>
          </Center>
          {secondPlayer && (
            <Center>
              <IconUsers size="1.05rem" className={classes.icon} stroke={1.5} />
              <Badge variant="outline" className="ml-2">
                <Link href={`/players/${secondPlayer.id}`}>
                  {secondPlayer.name}
                </Link>
              </Badge>
            </Center>
          )}
        </Group>
      </Card.Section>

      <Card.Section className={classes.section}>
        <Center>
          <Button
            size="xs"
            radius="xl"
            variant="gradient"
            gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
            onClick={(e) => {
              e.preventDefault()
              router.push(`/teams/${id}`)
            }}
          >
            Visit Team Page
          </Button>
        </Center>
      </Card.Section>
    </Card>
  )
}
