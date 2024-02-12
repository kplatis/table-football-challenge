import {
  Text,
  Card,
  Center,
  Stack,
  Title,
  SimpleGrid,
  UnstyledButton,
} from '@mantine/core'
import { IconCreditCard } from '@tabler/icons-react'
import classes from './page.module.css'

export default function GameCreatePage() {
  return (
    <Stack gap="lg">
      <Center>
        <Title order={1}>Create New Game</Title>
      </Center>
      <Card withBorder radius="md">
        <SimpleGrid cols={2} mt="md">
          <UnstyledButton className={classes.item}>
            <IconCreditCard color="blue" size="2rem" />
            <Text size="xs" mt={7}>
              Already Played Game
            </Text>
          </UnstyledButton>
          <UnstyledButton className={classes.item}>
            <IconCreditCard color="blue" size="2rem" />
            <Text size="xs" mt={7}>
              Live Game
            </Text>
          </UnstyledButton>
        </SimpleGrid>
      </Card>
    </Stack>
  )
}
