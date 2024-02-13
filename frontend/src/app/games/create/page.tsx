import {
  Text,
  Card,
  Stack,
  Title,
  SimpleGrid,
  UnstyledButton,
} from '@mantine/core'
import { IconBallFootball, IconPlayFootball } from '@tabler/icons-react'
import classes from './page.module.css'

export default function GameCreatePage() {
  return (
    <Stack gap="lg">
      <Title order={1} ta="center" m="xl">
        Create New Game
      </Title>
      <Card withBorder radius="md">
        <SimpleGrid cols={2} mt="md">
          <UnstyledButton className={classes.item}>
            <IconBallFootball color="blue" size="2rem" />
            <Text size="xs" mt={7}>
              Already Played Game
            </Text>
          </UnstyledButton>
          <UnstyledButton className={classes.item}>
            <IconPlayFootball color="blue" size="2rem" />
            <Text size="xs" mt={7}>
              Live Game
            </Text>
          </UnstyledButton>
        </SimpleGrid>
      </Card>
    </Stack>
  )
}
