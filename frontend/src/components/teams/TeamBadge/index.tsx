import { Player } from '@/types/players'
import { Badge, Center, Group } from '@mantine/core'
import { IconUsers } from '@tabler/icons-react'
import Link from 'next/link'
import classes from './TeamBadge.module.css'

type Props = {
  firstPlayer: Player
  secondPlayer: Player | null
}

export default function TeamBadge({ firstPlayer, secondPlayer }: Props) {
  return (
    <Group gap={8} mb={-8}>
      <Center>
        <IconUsers size="1.05rem" className={classes.icon} stroke={1.5} />
        <Badge variant="outline" className="ml-2">
          <Link href={`/players/${firstPlayer.id}`}>{firstPlayer.name}</Link>
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
  )
}
